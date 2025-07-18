import pygame
from pygame.locals import *
import math

class Quadtree:
    def __init__(self, boundary, capacity):
        self.boundary = boundary
        self.capacity = capacity
        self.points = []
        self.divided = False

    def subdivide(self):
        x, y, w, h = self.boundary
        hw, hh = w // 2, h // 2
        self.nw = Quadtree(pygame.Rect(x, y, hw, hh), self.capacity)
        self.ne = Quadtree(pygame.Rect(x + hw, y, hw, hh), self.capacity)
        self.sw = Quadtree(pygame.Rect(x, y + hh, hw, hh), self.capacity)
        self.se = Quadtree(pygame.Rect(x + hw, y + hh, hw, hh), self.capacity)
        self.divided = True

    def insert(self, point_data):
        x, y = point_data[:2]
        if not self.boundary.collidepoint(x, y):
            return False
        if len(self.points) < self.capacity:
            self.points.append(point_data)
            return True
        if not self.divided:
            self.subdivide()
        return (self.nw.insert(point_data) or self.ne.insert(point_data) or 
                self.sw.insert(point_data) or self.se.insert(point_data))

    def query(self, range_rect, found=None):
        if found is None:
            found = []
        if not self.boundary.colliderect(range_rect):
            return found
        for point_data in self.points:
            x, y = point_data[:2]
            if range_rect.collidepoint(x, y):
                found.append(point_data)
        if self.divided:
            self.nw.query(range_rect, found)
            self.ne.query(range_rect, found)
            self.sw.query(range_rect, found)
            self.se.query(range_rect, found)
        return found

    def clear(self):
        self.points = []
        if self.divided:
            self.nw.clear()
            self.ne.clear()
            self.sw.clear()
            self.se.clear()
        self.divided = False

    def draw_debug(self, surface):
        pygame.draw.rect(surface, (100, 100, 255), self.boundary, 1)
        if self.divided:
            self.nw.draw_debug(surface)
            self.ne.draw_debug(surface)
            self.sw.draw_debug(surface)
            self.se.draw_debug(surface)

# Constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
FIELD_WIDTH, FIELD_HEIGHT = 1000, 600
BALL_RADIUS, PLAYER_RADIUS = 10, 15
BALL_SPEED, PLAYER_SPEED = 4, 4
POSSE_DISTANCE = 30
SLICE_TIME = 100

class Campo:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.players_quadtree = Quadtree(self.rect, 4)

    def update_players_quadtree(self, jogadores):
        self.players_quadtree.clear()
        for i, jogador in enumerate(jogadores):
            self.players_quadtree.insert((jogador.x, jogador.y, i + 1))

    def find_ball_possession(self, bola):
        search_radius = POSSE_DISTANCE
        search_area = pygame.Rect(
            bola.x - search_radius, 
            bola.y - search_radius,
            search_radius * 2, 
            search_radius * 2
        )
        
        nearby_players = self.players_quadtree.query(search_area)
        
        closest_player = None
        min_distance = float('inf')
        
        for player_data in nearby_players:
            px, py, player_id = player_data
            distance = math.sqrt((bola.x - px) ** 2 + (bola.y - py) ** 2)
            
            if distance <= POSSE_DISTANCE and distance < min_distance:
                min_distance = distance
                closest_player = player_id
        
        return closest_player

    def draw(self, surface):
        # Campo verde
        pygame.draw.rect(surface, (34, 139, 34), self.rect)
        
        # Bordas do campo
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 5)
        
        # Círculo central
        cx, cy = self.rect.center
        pygame.draw.circle(surface, (255, 255, 255), (cx, cy), 60, 3)
        
        # Linha central
        pygame.draw.line(surface, (255, 255, 255), (cx, self.rect.top), (cx, self.rect.bottom), 3)
        
        # Áreas dos gols
        goal_area_w, goal_area_h = 120, 360
        pygame.draw.rect(surface, (255, 255, 255), 
                        pygame.Rect(self.rect.left, cy - goal_area_h//2, goal_area_w, goal_area_h), 3)
        pygame.draw.rect(surface, (255, 255, 255), 
                        pygame.Rect(self.rect.right - goal_area_w, cy - goal_area_h//2, goal_area_w, goal_area_h), 3)

    def verificar_gol(self, bola):
        goal_area_h = 360
        cy = self.rect.centery
        
        if bola.x + BALL_RADIUS <= self.rect.left:
            if cy - goal_area_h//2 <= bola.y <= cy + goal_area_h//2:
                return "direita"
        elif bola.x - BALL_RADIUS >= self.rect.right:
            if cy - goal_area_h//2 <= bola.y <= cy + goal_area_h//2:
                return "esquerda"
        elif bola.y + BALL_RADIUS <= self.rect.top or bola.y - BALL_RADIUS >= self.rect.bottom:
            return "Out"
        
        return "In"

class Bola:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (int(self.x), int(self.y)), BALL_RADIUS)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Jogador:
    def __init__(self, x, y, numero, cor):
        self.x, self.y = float(x), float(y)
        self.numero = numero
        self.cor = cor
        self.has_ball = False

    def draw(self, surface):
        # Destaque se tem a posse da bola
        if self.has_ball:
            pygame.draw.circle(surface, (255, 255, 0), (int(self.x), int(self.y)), PLAYER_RADIUS + 5, 3)
        
        # Corpo do jogador
        pygame.draw.circle(surface, self.cor, (int(self.x), int(self.y)), PLAYER_RADIUS)
        
        # Número do jogador
        font = pygame.font.SysFont(None, 18)
        num_text = font.render(str(self.numero), True, (0, 0, 0))
        text_rect = num_text.get_rect(center=(int(self.x), int(self.y)))
        surface.blit(num_text, text_rect)

    def move(self, dx, dy, campo):
        new_x = max(campo.rect.left + PLAYER_RADIUS, 
                   min(self.x + dx, campo.rect.right - PLAYER_RADIUS))
        new_y = max(campo.rect.top + PLAYER_RADIUS, 
                   min(self.y + dy, campo.rect.bottom - PLAYER_RADIUS))
        self.x, self.y = new_x, new_y

def create_teams():
    jogadores = []
    
    # Posições base para formação 4-3-3 ajustadas
    campo_rect = pygame.Rect((SCREEN_WIDTH-FIELD_WIDTH)//2, (SCREEN_HEIGHT-FIELD_HEIGHT)//2, FIELD_WIDTH, FIELD_HEIGHT)
    
    # Time Amarelo (esquerda) - posições ajustadas
    positions_yellow = [
        (campo_rect.left + 80, campo_rect.centery),  # Goleiro
        (campo_rect.left + 200, campo_rect.top + 130),  # Defesa
        (campo_rect.left + 200, campo_rect.top + 230),
        (campo_rect.left + 200, campo_rect.bottom - 230),
        (campo_rect.left + 200, campo_rect.bottom - 130),
        (campo_rect.left + 350, campo_rect.top + 180),  # Meio
        (campo_rect.left + 350, campo_rect.centery),
        (campo_rect.left + 350, campo_rect.bottom - 180),
        (campo_rect.left + 480, campo_rect.top + 160),  # Ataque - ajustado para não sobrepor
        (campo_rect.left + 480, campo_rect.centery),
        (campo_rect.left + 480, campo_rect.bottom - 160),
    ]
    
    for i, (x, y) in enumerate(positions_yellow):
        jogadores.append(Jogador(x, y, i + 1, (255, 255, 0)))
    
    # Time Azul (direita) - posições ajustadas
    positions_blue = [
        (campo_rect.right - 80, campo_rect.centery),  # Goleiro
        (campo_rect.right - 200, campo_rect.top + 130),  # Defesa
        (campo_rect.right - 200, campo_rect.top + 230),
        (campo_rect.right - 200, campo_rect.bottom - 230),
        (campo_rect.right - 200, campo_rect.bottom - 130),
        (campo_rect.right - 350, campo_rect.top + 180),  # Meio
        (campo_rect.right - 350, campo_rect.centery),
        (campo_rect.right - 350, campo_rect.bottom - 180),
        (campo_rect.right - 480, campo_rect.top + 160),  # Ataque - ajustado para não sobrepor
        (campo_rect.right - 480, campo_rect.centery),
        (campo_rect.right - 480, campo_rect.bottom - 160),
    ]
    
    for i, (x, y) in enumerate(positions_blue):
        jogadores.append(Jogador(x, y, i + 12, (0, 191, 255)))
    
    return jogadores

def generate_heatmap(surface, player_positions_history, field_rect, cell_size=20, target_player_id=None):
    """Gera e desenha um mapa de calor das posições dos jogadores."""
    heatmap_data = {}
    max_count = 0

    for x in range(field_rect.left, field_rect.right, cell_size):
        for y in range(field_rect.top, field_rect.bottom, cell_size):
            heatmap_data[(x, y)] = 0

    for frame_positions in player_positions_history:
        for player_id, (px, py) in frame_positions.items():
            if target_player_id is None or player_id == target_player_id:
                cell_x = int((px - field_rect.left) // cell_size) * cell_size + field_rect.left
                cell_y = int((py - field_rect.top) // cell_size) * cell_size + field_rect.top
                cell_x = max(field_rect.left, min(cell_x, field_rect.right - cell_size))
                cell_y = max(field_rect.top, min(cell_y, field_rect.bottom - cell_size))
                heatmap_data[(cell_x, cell_y)] = heatmap_data.get((cell_x, cell_y), 0) + 1
                if heatmap_data[(cell_x, cell_y)] > max_count:
                    max_count = heatmap_data[(cell_x, cell_y)]

    for (x, y), count in heatmap_data.items():
        if count > 0:
            alpha = int(255 * (count / max_count)) if max_count > 0 else 0
            pygame.draw.rect(surface, (255, 0, 0, alpha), (x, y, cell_size, cell_size))

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Futebol com Quadtree - Posse de Bola e Heatmap")
    clock = pygame.time.Clock()
    
    # Inicialização
    campo = Campo((SCREEN_WIDTH-FIELD_WIDTH)//2, (SCREEN_HEIGHT-FIELD_HEIGHT)//2, FIELD_WIDTH, FIELD_HEIGHT)
    bola = Bola(SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
    jogadores = create_teams()
    
    placar = {"esquerda": 0, "direita": 0}
    selected_player = None
    current_ball_owner = None
    show_quadtree_debug = False
    
    # Variáveis do heatmap
    player_positions_history = []
    show_heatmap = False
    individual_heatmap = False
    current_player_id = 1
    last_slice = pygame.time.get_ticks()
    
    running = True
    while running:
        # Eventos
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for jogador in jogadores:
                    if math.sqrt((mx - jogador.x)**2 + (my - jogador.y)**2) <= PLAYER_RADIUS:
                        selected_player = jogador
                        break
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    show_quadtree_debug = not show_quadtree_debug
                elif event.key == pygame.K_h:
                    show_heatmap = not show_heatmap
                    individual_heatmap = False
                elif event.key == pygame.K_n and show_heatmap:
                    individual_heatmap = True
                    current_player_id += 1
                    if current_player_id > len(jogadores):
                        current_player_id = 1
        
        # Controles
        keys = pygame.key.get_pressed()
        
        # Movimentação da bola
        if keys[K_w]: bola.move(0, -BALL_SPEED)
        if keys[K_s]: bola.move(0, BALL_SPEED)
        if keys[K_a]: bola.move(-BALL_SPEED, 0)
        if keys[K_d]: bola.move(BALL_SPEED, 0)
        
        # Movimentação do jogador selecionado
        if selected_player:
            if keys[K_UP]: selected_player.move(0, -PLAYER_SPEED, campo)
            if keys[K_DOWN]: selected_player.move(0, PLAYER_SPEED, campo)
            if keys[K_LEFT]: selected_player.move(-PLAYER_SPEED, 0, campo)
            if keys[K_RIGHT]: selected_player.move(PLAYER_SPEED, 0, campo)
        
        # Salva posições dos jogadores para heatmap
        now = pygame.time.get_ticks()
        if now - last_slice >= SLICE_TIME:
            frame_positions = {i+1: (jogador.x, jogador.y) for i, jogador in enumerate(jogadores)}
            player_positions_history.append(frame_positions)
            last_slice = now
        
        # Atualiza quadtree e detecta posse de bola
        campo.update_players_quadtree(jogadores)
        current_ball_owner = campo.find_ball_possession(bola)
        
        # Atualiza status de posse dos jogadores
        for jogador in jogadores:
            jogador.has_ball = (jogador.numero == current_ball_owner)
        
        # Verificação de gol
        status = campo.verificar_gol(bola)
        if status in ["esquerda", "direita"]:
            placar[status] += 1
            bola.x, bola.y = SCREEN_WIDTH//2, SCREEN_HEIGHT//2
        
        # Desenho
        screen.fill((0, 100, 0))
        campo.draw(screen)
        
        # Debug da quadtree
        if show_quadtree_debug:
            campo.players_quadtree.draw_debug(screen)
        
        # Heatmap
        if show_heatmap:
            heatmap_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
            if individual_heatmap:
                generate_heatmap(heatmap_surface, player_positions_history, campo.rect, target_player_id=current_player_id)
            else:
                generate_heatmap(heatmap_surface, player_positions_history, campo.rect)
            screen.blit(heatmap_surface, (0, 0))
        
        bola.draw(screen)
        
        for jogador in jogadores:
            jogador.draw(screen)
        
        # Interface
        font = pygame.font.SysFont(None, 28)
        placar_txt = font.render(f"Placar: {placar['esquerda']} x {placar['direita']} | Status: {status}", True, (255, 255, 255))
        screen.blit(placar_txt, (20, 20))
        
        # **FUNCIONALIDADE PRINCIPAL: Mostra posse de bola no centro superior**
        if current_ball_owner:
            font_posse = pygame.font.SysFont(None, 40)
            posse_txt = font_posse.render(f"POSSE DE BOLA: JOGADOR {current_ball_owner}", True, (255, 255, 255))
            posse_rect = posse_txt.get_rect(center=(SCREEN_WIDTH//2, 80))
            
            # Fundo destacado
            bg_rect = pygame.Rect(posse_rect.left - 15, posse_rect.top - 8, posse_rect.width + 30, posse_rect.height + 16)
            pygame.draw.rect(screen, (0, 0, 0), bg_rect)
            pygame.draw.rect(screen, (255, 255, 0), bg_rect, 3)
            
            screen.blit(posse_txt, posse_rect)
            
            # Linha conectando bola ao jogador
            jogador_com_posse = next(j for j in jogadores if j.numero == current_ball_owner)
            pygame.draw.line(screen, (255, 255, 0), 
                           (int(bola.x), int(bola.y)), 
                           (int(jogador_com_posse.x), int(jogador_com_posse.y)), 2)
        else:
            font_sem_posse = pygame.font.SysFont(None, 32)
            sem_posse_txt = font_sem_posse.render("BOLA LIVRE", True, (200, 200, 200))
            sem_posse_rect = sem_posse_txt.get_rect(center=(SCREEN_WIDTH//2, 80))
            screen.blit(sem_posse_txt, sem_posse_rect)
        
        # Mostra o número do jogador se for heatmap individual
        if show_heatmap and individual_heatmap:
            font = pygame.font.SysFont(None, 36)
            txt = font.render(f"Heatmap Jogador {current_player_id}", True, (255, 255, 0))
            screen.blit(txt, (SCREEN_WIDTH//2-120, 120))
        
        # Instruções
        font_small = pygame.font.SysFont(None, 20)
        instructions = [
            "WASD: Mover bola | Setas: Mover jogador selecionado",
            "Q: Toggle debug quadtree | Click: Selecionar jogador",
            "H: Toggle heatmap | N: Próximo jogador (heatmap individual)",
            f"Distância para posse: {POSSE_DISTANCE}px"
        ]
        
        for i, instruction in enumerate(instructions):
            txt = font_small.render(instruction, True, (255, 255, 255))
            screen.blit(txt, (20, SCREEN_HEIGHT - 100 + i * 25))
        
        pygame.display.flip()
        clock.tick(60)
    
    # Salva heatmap ao sair
    try:
        heatmap_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        generate_heatmap(heatmap_surface, player_positions_history, campo.rect)
        pygame.image.save(heatmap_surface, "heatmap_jogadores.png")
        print("Heatmap salvo como 'heatmap_jogadores.png'")
    except:
        print("Erro ao salvar heatmap")
    
    pygame.quit()

if __name__ == "__main__":
    main()

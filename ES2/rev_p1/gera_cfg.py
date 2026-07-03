from pathlib import Path 
import argparse
from py2cfg import CFGBuilder

parser = argparse.ArgumentParser(
   description="Gera o CFG de um programa Python"
)
parser.add_argument("programa", help="arquivo .py de entrada")
parser.add_argument("saida", help="diretorio de saida")
args = parser.parse_args()
programa = Path(args.programa)
saida = Path(args.saida)
saida.mkdir(parents=True, exist_ok=True)
cfg_name = programa.stem
cfg = CFGBuilder().build_from_file(cfg_name, str(programa))
cfg.build_visual(cfg_name, "pdf", directory=str(saida))
print(f"CFG gerado em: {saida / (cfg_name + '.pdf')}")

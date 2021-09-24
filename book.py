import chess
import random

infinity = float('inf')
# Le répertoire d'ouvertures de TSCP. Je l'ai repris et converti pour qu'il soit utilisable en Python. Je l'ai converti avec Python, mais pas avect ce fichier. Pour cette grosse liste, j'admets ne pas avoir respecté les 80 carractères par lignes :)
tscp_op = [['g1f3', 'g8f6', 'c2c4', 'b7b6', 'g2g3'], ['g1f3', 'g8f6', 'c2c4', 'c7c5', 'b1c3', 'b8c6'], ['g1f3', 'g8f6', 'c2c4', 'c7c5', 'b1c3', 'e7e6', 'g2g3', 'b7b6', 'f1g2', 'c8b7', 'e1g1', 'f8e7'], ['g1f3', 'g8f6', 'c2c4', 'c7c5', 'g2g3'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'b8d7'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8b4'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c6', 'c1g5'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c5'], ['g1f3', 'g8f6', 'c2c4', 'e7e6', 'g2g3', 'd7d5', 'f1g2', 'f8e7'], ['g1f3', 'g8f6', 'c2c4', 'g7g6', 'b1c3', 'f8g7', 'e2e4'], ['g1f3', 'g8f6', 'c2c4', 'g7g6', 'g2g3', 'f8g7', 'f1g2', 'e8g8'], ['g1f3', 'g8f6', 'd2d4', 'c7c5'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'd5c4', 'a2a4', 'c8f5', 'e2e3', 'e7e6', 'f1c4'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'c1g5'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'c7c6', 'e2e3'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'd5c4', 'e2e3', 'e7e6', 'f1c4', 'c7c5', 'e1g1', 'a7a6'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'b8d7'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8b4'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'c1g5'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c5'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'c1g5'], ['g1f3', 'g8f6', 'd2d4', 'd7d5', 'c2c4', 'e7e6', 'g2g3'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c1g5'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'f8b4', 'b1d2'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'f8b4', 'c1d2'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'b7b6', 'b1c3', 'c8b7', 'a2a3', 'd7d5', 'c4d5', 'f6d5'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'b7b6', 'b1c3', 'f8b4'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'b7b6', 'a2a3', 'c8b7', 'b1c3', 'd7d5', 'c4d5', 'f6d5'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'b7b6', 'g2g3', 'c8b7', 'f1g2', 'f8e7', 'e1g1', 'e8g8', 'b1c3', 'f6e4', 'd1c2', 'e4c3', 'c2c3'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'b7b6', 'g2g3', 'c8a6', 'b2b3', 'f8b4', 'c1d2', 'b4e7'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'c7c5', 'd4d5', 'e6d5', 'c4d5', 'd7d6', 'b1c3', 'g7g6'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'b8d7'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8b4'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c6', 'c1g5'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c5'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'c1g5'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'c2c4', 'd7d5', 'g2g3'], ['g1f3', 'g8f6', 'd2d4', 'e7e6', 'g2g3'], ['g1f3', 'g8f6', 'd2d4', 'g7g6', 'c1g5'], ['g1f3', 'g8f6', 'd2d4', 'g7g6', 'c2c4', 'f8g7', 'b1c3', 'e8g8', 'e2e4', 'd7d6', 'f1e2', 'e7e5', 'e1g1', 'b8c6', 'd4d5', 'c6e7', 'f3e1', 'f6d7'], ['g1f3', 'g8f6', 'd2d4', 'g7g6', 'c2c4', 'f8g7', 'g2g3', 'e8g8', 'f1g2', 'd7d6', 'e1g1'], ['g1f3', 'g8f6', 'd2d4', 'g7g6', 'g2g3', 'f8g7', 'f1g2', 'e8g8'], ['g1f3', 'g8f6', 'g2g3', 'g7g6'], ['g1f3', 'c7c5', 'c2c4', 'b8c6'], ['g1f3', 'c7c5', 'c2c4', 'g8f6', 'b1c3', 'b8c6'], ['g1f3', 'c7c5', 'c2c4', 'g8f6', 'b1c3', 'e7e6', 'g2g3', 'b7b6', 'f1g2', 'c8b7', 'e1g1', 'f8e7'], ['g1f3', 'c7c5', 'c2c4', 'g8f6', 'g2g3'], ['g1f3', 'd7d5', 'c2c4'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'd5c4', 'a2a4', 'c8f5', 'e2e3', 'e7e6', 'f1c4'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'c1g5'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'c7c6', 'e2e3'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'd5c4', 'e2e3', 'e7e6', 'f1c4', 'c7c5', 'e1g1', 'a7a6'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'b8d7'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'c1g5'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c5'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'c1g5'], ['g1f3', 'd7d5', 'd2d4', 'g8f6', 'c2c4', 'e7e6', 'g2g3'], ['g1f3', 'd7d5', 'g2g3'], ['g1f3', 'g7g6'], ['c2c4', 'g8f6', 'b1c3', 'c7c5'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'b8d7'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'f8b4'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'c7c6', 'c1g5'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3', 'd7d5', 'd2d4', 'c7c5'], ['c2c4', 'g8f6', 'b1c3', 'e7e5', 'g1f3', 'b8c6', 'g2g3'], ['c2c4', 'g8f6', 'b1c3', 'g7g6'], ['c2c4', 'g8f6', 'g1f3', 'b7b6', 'g2g3'], ['c2c4', 'g8f6', 'g1f3', 'c7c5', 'b1c3', 'b8c6'], ['c2c4', 'g8f6', 'g1f3', 'c7c5', 'b1c3', 'e7e6', 'g2g3', 'b7b6', 'f1g2', 'c8b7', 'e1g1', 'f8e7'], ['c2c4', 'g8f6', 'g1f3', 'c7c5', 'g2g3'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'b8d7'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8b4'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c6', 'c1g5'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c5'], ['c2c4', 'g8f6', 'g1f3', 'e7e6', 'g2g3', 'd7d5', 'f1g2', 'f8e7'], ['c2c4', 'g8f6', 'g1f3', 'g7g6', 'b1c3', 'f8g7', 'e2e4'], ['c2c4', 'g8f6', 'g1f3', 'g7g6', 'g2g3', 'f8g7', 'f1g2', 'e8g8'], ['c2c4', 'c7c6'], ['c2c4', 'c7c5', 'g1f3', 'b8c6'], ['c2c4', 'c7c5', 'g1f3', 'g8f6', 'b1c3', 'b8c6'], ['c2c4', 'c7c5', 'g1f3', 'g8f6', 'b1c3', 'e7e6', 'g2g3', 'b7b6', 'f1g2', 'c8b7', 'e1g1', 'f8e7'], ['c2c4', 'c7c5', 'g1f3', 'g8f6', 'g2g3'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'g1f3', 'g8f6', 'c1f4', 'e8g8', 'e2e3'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'g1f3', 'g8f6', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'f8e7', 'g1f3', 'g8f6', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'c1g5', 'f8e7', 'e2e3'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'b8d7'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'f8b4'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'c7c6', 'c1g5'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'g1f3', 'c7c5'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'g8f6', 'c4d5', 'e6d5', 'c1g5'], ['c2c4', 'e7e6', 'b1c3', 'd7d5', 'd2d4', 'c7c6'], ['c2c4', 'e7e6', 'g1f3'], ['c2c4', 'e7e5', 'b1c3', 'b8c6'], ['c2c4', 'e7e5', 'b1c3', 'g8f6', 'g1f3', 'b8c6', 'g2g3'], ['c2c4', 'e7e5', 'g2g3'], ['c2c4', 'g7g6', 'b1c3'], ['d2d4', 'g8f6', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'c7c5'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'd5c4', 'a2a4', 'c8f5', 'e2e3', 'e7e6', 'f1c4'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'c7c6', 'e2e3'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'd5c4', 'e2e3', 'e7e6', 'f1c4', 'c7c5', 'e1g1', 'a7a6'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'b8d7'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8b4'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c5'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'd7d5', 'c2c4', 'e7e6', 'g2g3'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'f8b4', 'b1d2'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'f8b4', 'c1d2'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'b7b6', 'b1c3', 'c8b7', 'a2a3', 'd7d5', 'c4d5', 'f6d5'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'b7b6', 'b1c3', 'f8b4'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'b7b6', 'a2a3', 'c8b7', 'b1c3', 'd7d5', 'c4d5', 'f6d5'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'b7b6', 'g2g3', 'c8b7', 'f1g2', 'f8e7', 'e1g1', 'e8g8', 'b1c3', 'f6e4', 'd1c2', 'e4c3', 'c2c3'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'b7b6', 'g2g3', 'c8a6', 'b2b3', 'f8b4', 'c1d2', 'b4e7'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'c7c5', 'd4d5', 'e6d5', 'c4d5', 'd7d6', 'b1c3', 'g7g6'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'b8d7'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'f8b4'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c6', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'b1c3', 'c7c5'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'c2c4', 'd7d5', 'g2g3'], ['d2d4', 'g8f6', 'g1f3', 'e7e6', 'g2g3'], ['d2d4', 'g8f6', 'g1f3', 'g7g6', 'c1g5'], ['d2d4', 'g8f6', 'g1f3', 'g7g6', 'c2c4', 'f8g7', 'b1c3', 'e8g8', 'e2e4', 'd7d6', 'f1e2', 'e7e5', 'e1g1', 'b8c6', 'd4d5', 'c6e7', 'f3e1', 'f6d7'], ['d2d4', 'g8f6', 'g1f3', 'g7g6', 'c2c4', 'f8g7', 'g2g3', 'e8g8', 'f1g2', 'd7d6', 'e1g1'], ['d2d4', 'g8f6', 'g1f3', 'g7g6', 'g2g3', 'f8g7', 'f1g2', 'e8g8'], ['d2d4', 'g8f6', 'c2c4', 'c7c5', 'd4d5', 'b7b5', 'c4b5', 'a7a6'], ['d2d4', 'g8f6', 'c2c4', 'c7c5', 'd4d5', 'e7e6', 'b1c3', 'e6d5', 'c4d5', 'd7d6'], ['d2d4', 'g8f6', 'c2c4', 'd7d6', 'b1c3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4', 'd1c2', 'e8g8'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4', 'g1f3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4', 'e2e3', 'b7b6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4', 'e2e3', 'c7c5', 'f1d3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4', 'e2e3', 'e8g8', 'f1d3', 'd7d5', 'g1f3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'c1g5', 'f8e7', 'e2e3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'b8d7'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'f8b4'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'c7c6', 'c1g5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'g1f3', 'c7c5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'd7d5', 'c4d5', 'e6d5', 'c1g5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'f8b4', 'b1d2'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'f8b4', 'c1d2'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'b7b6', 'b1c3', 'c8b7', 'a2a3', 'd7d5', 'c4d5', 'f6d5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'b7b6', 'b1c3', 'f8b4'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'b7b6', 'a2a3', 'c8b7', 'b1c3', 'd7d5', 'c4d5', 'f6d5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'b7b6', 'g2g3', 'c8b7', 'f1g2', 'f8e7', 'e1g1', 'e8g8', 'b1c3', 'f6e4', 'd1c2', 'e4c3', 'c2c3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'b7b6', 'g2g3', 'c8a6', 'b2b3', 'f8b4', 'c1d2', 'b4e7'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'c7c5', 'd4d5', 'e6d5', 'c4d5', 'd7d6', 'b1c3', 'g7g6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'b8d7'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'f8b4'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'c7c6', 'c1g5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'b1c3', 'c7c5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'c1g5'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g1f3', 'd7d5', 'g2g3'], ['d2d4', 'g8f6', 'c2c4', 'e7e6', 'g2g3', 'd7d5', 'f1g2'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'b1c3', 'f8g7', 'e2e4', 'd7d6', 'f1e2', 'e8g8', 'c1g5'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'b1c3', 'f8g7', 'e2e4', 'd7d6', 'f1e2', 'e8g8', 'g1f3', 'e7e5', 'e1g1', 'b8c6', 'd4d5', 'c6e7', 'f3e1', 'f6d7'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'b1c3', 'f8g7', 'e2e4', 'd7d6', 'g1f3', 'e8g8', 'f1e2', 'e7e5', 'e1g1', 'b8c6', 'd4d5', 'c6e7', 'f3e1', 'f6d7'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'b1c3', 'f8g7', 'e2e4', 'd7d6', 'f2f3', 'e8g8', 'c1e3'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'b1c3', 'd7d5', 'g1f3', 'f8g7', 'd1b3', 'd5c4', 'b3c4'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'b1c3', 'd7d5', 'c4d5', 'f6d5', 'e2e4', 'd5c3', 'b2c3', 'f8g7', 'f1c4'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'g1f3', 'f8g7', 'b1c3', 'e8g8', 'e2e4', 'd7d6', 'f1e2', 'e7e5', 'e1g1', 'b8c6', 'd4d5', 'c6e7', 'f3e1', 'f6d7'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'g1f3', 'f8g7', 'g2g3', 'e8g8', 'f1g2', 'd7d6', 'e1g1'], ['d2d4', 'g8f6', 'c2c4', 'g7g6', 'g2g3', 'f8g7', 'f1g2', 'e8g8'], ['d2d4', 'd7d6', 'e2e4', 'g8f6', 'b1c3', 'g7g6', 'f2f4', 'f8g7', 'g1f3'], ['d2d4', 'd7d6', 'e2e4', 'g7g6'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'd5c4', 'a2a4', 'c8f5', 'e2e3', 'e7e6', 'f1c4'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'c1g5'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'c7c6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'c7c6', 'e2e3'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'd5c4', 'e2e3', 'e7e6', 'f1c4', 'c7c5', 'e1g1', 'a7a6'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'b8d7'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'f8b4'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'c1g5'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'b1c3', 'c7c5'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'c1g5'], ['d2d4', 'd7d5', 'g1f3', 'g8f6', 'c2c4', 'e7e6', 'g2g3'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'g8f6', 'g1f3', 'd5c4', 'a2a4', 'c8f5', 'e2e3', 'e7e6', 'f1c4'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'g8f6', 'g1f3', 'e7e6', 'c1g5'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'g8f6', 'g1f3', 'e7e6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'g8f6', 'g1f3', 'e7e6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'b1c3', 'g8f6', 'e2e3'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'g1f3', 'g8f6', 'b1c3', 'd5c4', 'a2a4', 'c8f5', 'e2e3', 'e7e6', 'f1c4'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'g1f3', 'g8f6', 'b1c3', 'e7e6', 'c1g5'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'g1f3', 'g8f6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'g1f3', 'g8f6', 'b1c3', 'e7e6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'd7d5', 'c2c4', 'c7c6', 'g1f3', 'g8f6', 'e2e3'], ['d2d4', 'd7d5', 'c2c4', 'd5c4', 'g1f3', 'g8f6', 'e2e3', 'e7e6', 'f1c4', 'c7c5', 'e1g1', 'a7a6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'g1f3', 'g8f6', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'g1f3', 'g8f6', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'f8e7', 'g1f3', 'g8f6', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'c1g5', 'f8e7', 'e2e3'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'b8d7'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'f8b4'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'c7c6', 'c1g5'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'g1f3', 'c7c5'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'g8f6', 'c4d5', 'e6d5', 'c1g5'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'b1c3', 'c7c6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'b8d7'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'f8b4'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'c7c6', 'c1g5'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'b1c3', 'c7c5'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'c1g5'], ['d2d4', 'd7d5', 'c2c4', 'e7e6', 'g1f3', 'g8f6', 'g2g3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'f8b4', 'd1c2', 'e8g8'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'f8b4', 'g1f3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'f8b4', 'e2e3', 'b7b6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'f8b4', 'e2e3', 'c7c5', 'f1d3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'f8b4', 'e2e3', 'e8g8', 'f1d3', 'd7d5', 'g1f3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'c1g5', 'f8e7', 'e2e3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'b8d7'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'f8b4'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'c7c6', 'c1g5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'g1f3', 'c7c5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'b1c3', 'd7d5', 'c4d5', 'e6d5', 'c1g5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'f8b4', 'b1d2'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'f8b4', 'c1d2'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'b7b6', 'b1c3', 'c8b7', 'a2a3', 'd7d5', 'c4d5', 'f6d5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'b7b6', 'b1c3', 'f8b4'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'b7b6', 'a2a3', 'c8b7', 'b1c3', 'd7d5', 'c4d5', 'f6d5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'b7b6', 'g2g3', 'c8b7', 'f1g2', 'f8e7', 'e1g1', 'e8g8', 'b1c3', 'f6e4', 'd1c2', 'e4c3', 'c2c3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'b7b6', 'g2g3', 'c8a6', 'b2b3', 'f8b4', 'c1d2', 'b4e7'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'c7c5', 'd4d5', 'e6d5', 'c4d5', 'd7d6', 'b1c3', 'g7g6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'b8d7'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'f8e7', 'c1f4', 'e8g8', 'e2e3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'h7h6', 'g5h4', 'e8g8', 'e2e3', 'b7b6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'f8e7', 'c1g5', 'e8g8', 'e2e3', 'h7h6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'f8b4'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'c7c6', 'c1g5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'd1c2', 'f8d6'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'c7c6', 'e2e3', 'b8d7', 'f1d3', 'd5c4', 'd3c4', 'b7b5', 'c4d3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'b1c3', 'c7c5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'c1g5'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g1f3', 'd7d5', 'g2g3'], ['d2d4', 'e7e6', 'c2c4', 'g8f6', 'g2g3', 'd7d5', 'f1g2'], ['d2d4', 'f7f5'], ['d2d4', 'g7g6'], ['e2e4', 'g8f6', 'e4e5', 'f6d5', 'd2d4', 'd7d6', 'g1f3'], ['e2e4', 'c7c6', 'd2d4', 'd7d5', 'b1c3', 'd5e4', 'c3e4', 'b8d7'], ['e2e4', 'c7c6', 'd2d4', 'd7d5', 'b1c3', 'd5e4', 'c3e4', 'c8f5', 'e4g3', 'f5g6', 'h2h4', 'h7h6'], ['e2e4', 'c7c6', 'd2d4', 'd7d5', 'b1d2', 'd5e4', 'd2e4', 'b8d7'], ['e2e4', 'c7c6', 'd2d4', 'd7d5', 'b1d2', 'd5e4', 'd2e4', 'c8f5', 'e4g3', 'f5g6', 'h2h4', 'h7h6'], ['e2e4', 'c7c6', 'd2d4', 'd7d5', 'e4d5', 'c6d5', 'c2c4', 'g8f6', 'b1c3', 'e7e6', 'g1f3'], ['e2e4', 'c7c6', 'd2d4', 'd7d5', 'e4e5', 'c8f5'], ['e2e4', 'c7c5', 'b1c3', 'b8c6', 'g2g3', 'g7g6', 'f1g2', 'f8g7'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'f1b5'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'd7d6', 'c1g5', 'e7e6', 'd1d2', 'f8e7', 'e1c1', 'e8g8'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'd7d6', 'c1g5', 'e7e6', 'd1d2', 'a7a6', 'e1c1', 'h7h6'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'd7d6', 'f1c4'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'e7e5', 'd4b5', 'd7d6'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'd2d4', 'c5d4', 'f3d4', 'e7e6', 'b1c3', 'd8c7'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'd2d4', 'c5d4', 'f3d4', 'e7e6', 'b1c3', 'a7a6'], ['e2e4', 'c7c5', 'g1f3', 'b8c6', 'd2d4', 'c5d4', 'f3d4', 'g7g6'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'f1b5'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'b8c6', 'c1g5', 'e7e6', 'd1d2', 'f8e7', 'e1c1', 'e8g8'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'b8c6', 'c1g5', 'e7e6', 'd1d2', 'a7a6', 'e1c1', 'h7h6'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'b8c6', 'f1c4'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'a7a6', 'c1e3'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'a7a6', 'c1g5', 'e7e6', 'f2f4'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'a7a6', 'f1e2', 'e7e5', 'd4b3', 'f8e7'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'a7a6', 'f2f4'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'e7e6', 'f1e2'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'e7e6', 'g2g4'], ['e2e4', 'c7c5', 'g1f3', 'd7d6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'g7g6', 'c1e3', 'f8g7', 'f2f3'], ['e2e4', 'c7c5', 'g1f3', 'e7e6', 'b1c3'], ['e2e4', 'c7c5', 'g1f3', 'e7e6', 'd2d4', 'c5d4', 'f3d4', 'b8c6', 'b1c3', 'd8c7'], ['e2e4', 'c7c5', 'g1f3', 'e7e6', 'd2d4', 'c5d4', 'f3d4', 'b8c6', 'b1c3', 'a7a6'], ['e2e4', 'c7c5', 'g1f3', 'e7e6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'd7d6', 'f1e2'], ['e2e4', 'c7c5', 'g1f3', 'e7e6', 'd2d4', 'c5d4', 'f3d4', 'g8f6', 'b1c3', 'd7d6', 'g2g4'], ['e2e4', 'c7c5', 'g1f3', 'e7e6', 'd2d4', 'c5d4', 'f3d4', 'a7a6', 'f1d3'], ['e2e4', 'c7c5', 'c2c3'], ['e2e4', 'd7d6', 'd2d4', 'g8f6', 'b1c3', 'g7g6', 'f2f4', 'f8g7', 'g1f3'], ['e2e4', 'd7d6', 'd2d4', 'g7g6'], ['e2e4', 'd7d5', 'e4d5'], ['e2e4', 'e7e6', 'd2d4', 'd7d5', 'b1c3', 'f8b4', 'e4e5', 'c7c5', 'a2a3', 'b4c3', 'b2c3', 'g8e7'], ['e2e4', 'e7e6', 'd2d4', 'd7d5', 'b1c3', 'g8f6', 'c1g5'], ['e2e4', 'e7e6', 'd2d4', 'd7d5', 'b1d2', 'g8f6', 'e4e5'], ['e2e4', 'e7e6', 'd2d4', 'd7d5', 'b1d2', 'c7c5', 'g1f3'], ['e2e4', 'e7e6', 'd2d4', 'd7d5', 'b1d2', 'c7c5', 'e4d5', 'e6d5'], ['e2e4', 'e7e6', 'd2d4', 'd7d5', 'e4e5', 'c7c5', 'c2c3', 'b8c6', 'g1f3'], ['e2e4', 'e7e5', 'b1c3'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'b1c3', 'g8f6', 'f1b5'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4', 'f8c5'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1c4', 'g8f6'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'g8f6', 'e1g1'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5c6', 'd7c6', 'e1g1'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'g8f6', 'e1g1', 'f8e7', 'f1e1', 'b7b5', 'a4b3', 'd7d6', 'c2c3', 'e8g8', 'h2h3', 'c6b8', 'd2d4', 'b8d7'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'g8f6', 'e1g1', 'f8e7', 'f1e1', 'b7b5', 'a4b3', 'd7d6', 'c2c3', 'e8g8', 'h2h3', 'c6a5', 'b3c2', 'c7c5', 'd2d4', 'd8c7', 'b1d2'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'g8f6', 'e1g1', 'f8e7', 'f1e1', 'b7b5', 'a4b3', 'd7d6', 'c2c3', 'e8g8', 'h2h3', 'c8b7', 'd2d4', 'f8e8'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'g8f6', 'e1g1', 'f8e7', 'f1e1', 'b7b5', 'a4b3', 'e8g8', 'c2c3', 'd7d6', 'h2h3', 'c6b8', 'd2d4', 'b8d7'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'g8f6', 'e1g1', 'f8e7', 'f1e1', 'b7b5', 'a4b3', 'e8g8', 'c2c3', 'd7d6', 'h2h3', 'c6a5', 'b3c2', 'c7c5', 'd2d4', 'd8c7', 'b1d2'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'g8f6', 'e1g1', 'f8e7', 'f1e1', 'b7b5', 'a4b3', 'e8g8', 'c2c3', 'd7d6', 'h2h3', 'c8b7', 'd2d4', 'f8e8'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'g8f6', 'e1g1', 'f6e4', 'd2d4', 'b7b5', 'a4b3', 'd7d5', 'd4e5', 'c8e6', 'c2c3'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'f1b5', 'a7a6', 'b5a4', 'd7d6'], ['e2e4', 'e7e5', 'g1f3', 'b8c6', 'd2d4', 'e5d4', 'f3d4'], ['e2e4', 'e7e5', 'g1f3', 'g8f6', 'f3e5', 'd7d6', 'e5f3', 'f6e4', 'd2d4'], ['e2e4', 'e7e5', 'f2f4'], ['e2e4', 'g7g6', 'd2d4', 'f8g7', 'b1c3', 'd7d6'], ['g2g3']]


# Conversion du répertoire pour qu'il soit plus facilement utilisable.
book = [[[chess.Board().fen(), 'e2e4']]]
for openning in tscp_op :
    board = chess.Board()
    Openning = []
    for move in openning :
        board.push(chess.Move.from_uci(move))
        a = board.fen()
        try :
            Move = openning[openning.index(move)+1]
        except Exception :
            Move = None
        Openning.append([a, Move])
    book.append(Openning)

def move_from_book(the_board, book) :
    '''Renvoie un mouvement du répertoire si la position y est.'''
    liste = []
    for start in book :
        for couple in start :
            if is_equivalent(couple[0], the_board) :
                liste.append(couple[1])
    try :
        return random.choice(liste)
    except Exception :
        return None

def is_equivalent(fen, board2) :
    '''Détermine si deux positions sont équivalentes. Je ne pouvais pas utiliser le FEN, car une partie peut être au coup 5 et l'autre au coup 15, elles peuvent être équivalents.'''
    board1 = chess.Board(fen)
    for case in chess.SQUARES :
        if board1.piece_at(case) != board2.piece_at(case) :
            return False
    return True
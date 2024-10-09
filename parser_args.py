#common modul
import argparse
# import os
import sys

def parser_batik():
    ''' parser collection '''
    ap = argparse.ArgumentParser(description='generate batik')
    ap.add_argument("--argument", required=False)
    
    ap.add_argument("-n", "--n_epochs", type=int, default=2, help="number of epoch for training")#100
    ap.add_argument("-b", "--batch_size", type=int, default=1, help="batch size of training")#1
    ap.add_argument("-i", '--interval', type=int, default=1, help='interval')#5
    ap.add_argument('-ds', '--dataset', type=str, default="datasets/Taiganja", help='path to the dataset')

    
    args=ap.parse_args()
    
    return (args)

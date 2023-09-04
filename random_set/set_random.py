import random
import numpy
import torch

def set_random_seed(seed):
    """Set random seed for reproducibility."""
    random.seed(seed)
    numpy.random.seed(seed)
    torch.manual_seed(seed)


def main():
    args = 123
    result = set_random_seed(args)
    return result

if __name__ == "__main__":
    main()
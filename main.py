from Individu import *

def main():
    ind = Individu()
    ind.generate_phrase(8)
    print(ind.get_phrase())


if __name__ == '__main__':
    main()


import block

DIFF = 3               # change if you want faster block creation

def main():

    # generate genisis block
    genisis_block = block.create_first_block(DIFF)
    next_block = block.create_next_block(genisis_block)
    


if __name__ == '__main__':
    main()
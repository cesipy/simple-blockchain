import block

DIFF = 4                # change if you want faster block creation

def main():

    # generate genisis block
    genisis_block = block.create_first_block(DIFF)
    block.proof_of_work(genisis_block)


if __name__ == '__main__':
    main()
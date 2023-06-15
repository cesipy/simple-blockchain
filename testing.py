import block

DIFF = 3

def main():

    # generate genisis block
    genisis_block = block.create_first_block(DIFF)
    block.proof_of_work(genisis_block)


main()
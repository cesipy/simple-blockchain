import block

DIFF = 3               # change if you want faster block creation

def main():

    # generate genisis block
    genisis_block = block.create_first_block(DIFF)
    previous_block = genisis_block
    print(previous_block, '\n')
    
    # create
    for i in range(5):
        current_block = block.create_next_block(previous_block)
        print(current_block, '\n')
        previous_block = current_block



if __name__ == '__main__':
    main()
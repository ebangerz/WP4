import api
import visual


def main():

    meme = False

    def run():
        top_text = str(input('What would you like your top text to say?: '))
        bottom_text = str(input('What would you like your bottom text to say?: '))
        print('Generating meme...')
        print('Close or save meme to proceed.')
        visual.print_img(api.return_info(top_text, bottom_text))

    while True:
        entry = input('Would you like to create a meme? (y) for yes and (q) to quit: ')
        if entry.lower() == 'y':
            meme = True
            break
        elif entry.lower() == 'q':
            break
        else:
            print('Not a valid option. Try again!')


    run()
    while meme:
        while True:
            cont = input(('Create another? (y) for yes or (q) to quit: '))

            if cont.lower == 'y':
                run()
            elif cont.lower() == 'q':
                break
        # else:
        #     print('Not a valid option! Try again!')
        #     pass
            


if __name__ == '__main__':
    main()
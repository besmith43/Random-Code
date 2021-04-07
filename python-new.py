#!/usr/bin/env python3

import os
import argh

@argh.arg('--program-name', '-o', help="Name of the python program to be created")
def main(program_name=os.path.basename(os.getcwd())):
    name = program_name + ".py"

    if not os.path.exists(name):
        append_write = 'w'
    else:
        print("The program file already exists")
        exit(1)

    content = "import argh\n\ndef main():\n\nif __name__ == \"__main__\":\n    argh.dispatch_command(main)\n"
    program_file = open(name, append_write)
    program_file.write(content)
    program_file.close()

if __name__ == "__main__":
    argh.dispatch_command(main)

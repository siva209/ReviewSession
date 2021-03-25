from basescript import BaseScript


class Adder(BaseScript):
    # The following specifies the script description so that it be used
    # as a part of the usage doc when --help option is used during running.
    DESC = 'Adds numbers'

    def __init__(self):
        super(Adder, self).__init__()
        self.a = 10
        self.b = 20
        self.d="hello"


    def define_args(self, parser):
        """

        :param parser: Define script specific command-line arguments.
        @parser is a parser object created using the `argparse` modul

        :return:None
        """

        parser.add_argument('c', type=int, help='Number to add')
        # parser.add_argument('e', type=str, help='Number to add')

    def run(self):
        """
          Override this method to define logic for `run` sub-command

        """

        self.log.info("Starting run of script ...")
        print(self.a + self.b + self.args.c)

        # print(self.d+self.args.e)
        # self.log.info("Script is done")


if __name__ == '__main__':
    Adder().start()

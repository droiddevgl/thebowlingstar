import configparser
from configparser import ConfigParser

from Person import Person
from CheckingAccount import CheckingAccount
import logging

def main():
    print('in main')
    checking1 = CheckingAccount('Brandon', 500)
    checking1.withdraw(100)
    print(checking1.getStats())
    checking1.deposit(1000)
    print(checking1.getStats())

    checking2 = CheckingAccount('Josh', 1200)
    checking2.withdraw(100)
    print(checking2.getStats())
    checking2.deposit(1000)
    print(checking2.getStats())
    #print(checking1.getAccountType())
    #print(checking.amount)
    # person1 = Person("jakob",24)
    # person2 = Person("kim", 42)
    # person3 = Person("brendon", 28)
    # person4 = Person("victor", 52)
    #
    # print('\nperson1')
    # person1.setTitle("CEO")
    # print(person1.getStatus())
    # person2.setTitle("QA")
    # print('\nperson2')
    # person3.setTitle("student")
    # print(person2.getStatus())
    # person4.setTitle("teacher")
    # print('\nperson3')
    # print(person3.getStatus())
    # print('\nperson4')
    # print(person4.getStatus())

    # parsing a config file
    config = configparser.ConfigParser()

    config.read('config.ini')

    print(f'Sections of config: {config.sections()}')

    print(config.get('general','Name'))
    print(config.get('secret', 'secretid'))

    # handle logging - where will be the log file
    logging.basicConfig(filename='../main.log')

    logger = logging.getLogger()

    # info, error and critical will work ok
    logger.setLevel(logging.INFO)

    # there are couple of logger methods. info, debug, error, critical
    logger.info('This is info')
    logger.debug('This is debug')
    logger.error('This is error')
    logger.critical('This is critical')

    # debug level needs to be changed to debug for the debug log to work
    logger.setLevel(logging.DEBUG)
    logger.debug('This is debug')



    # error handling
    tmp_dict = {'Name': 'Brandon'}
    try:
        result = tmp_dict['Does not exist']
    except KeyError as e:
        print(f'Did not find original value {e}')
        result = tmp_dict['Name']
        #pass # - will supress the error. it will let it pass
        #raise e - will throw an error

    print(result)

if __name__ == '__main__':
    main()

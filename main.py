from linkList import LinkedList

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    link = LinkedList()
    link.ending(5)
    link.ending(15)
    link.print_list()
    print("在第一個節點插入新結點")
    link.beginning(10)
    link.print_list()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

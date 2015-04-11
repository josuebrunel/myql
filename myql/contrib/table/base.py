from xml.etree import cElementTree as ctree

class Base(object):

    def addElement(self, elt, tagName=None):
        pass

    def removeElement(self, elt, tagName=None):
        pass

    def addFunction(self, func_code, from_file=''):
        """Add function 
        """
        if from_file:
            with open(from_file) as f:
                func_code = f.read()

        root = self.etree
        t_execute = root.find('execute')

        if not t_execute :
            t_execute = ctree.SubElement(root, 'execute')

        t_execute.text = "\n ![CDATA] {0} ]]\n".format(func_code)

        return True

    def removeFunction(self):
        """Remove function tag
        """
        root = self.etree
        t_execute = root.find('execute')
        try:
            root.remove(t_execute)
            return True
        except Exception,e:
            print(e)

        return False

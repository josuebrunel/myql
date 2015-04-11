from xml.etree import cElementTree as ctree

class Base(object):

    def addElement(self, elt, tagName=None):
        root = self.etree
        t_elt = root.find(tagName)
        if not t_elt:
            t_elt = ctree.SubElement(root, tagName)

        root.append(t_elt)
        return True

    def removeElement(self, elt, tagName=None):
        root = self.etree
        t_elt = root.find(tagName)

        try:
            root.remove(t_elt)
            return True
        except Exception,e:
            print(e)

        return False

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

        t_execute.text = "\n\t![CDATA]{0:>5}]]\n\t".format(func_code.ljust(4))

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

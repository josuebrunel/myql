class Binder(object):
    """Class describing binders : select, insert, update, delete
    """

    def __init__(self, name, itemPath, produces, pollingFrequencySeconds=30):
        """Initializes the class
        """
        self.name = name
        self.itemPath = itemPath
        self.pollingFrequencySeconds = pollingFrequencySeconds
        self.produces = produces

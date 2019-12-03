class IndexedFile:
    def __init__(self, data: dict):
        self.id = data.get('_id', None) if data.get('_id', None) is not None else data.get('id', None),
        self.indexes = data.get('indexes', None),
        self.title = data.get('title', None),
        self.created = data.get('created', None),
        self.updated = data.get('updated', None),
        self.onwner = data.get('onwner', None),
        self.updater = data.get('updater', None),
        self.file = data.get('file', None),
        self.status = data.get('status', None),
        self.replacedBy = data.get('replacedBy', None)
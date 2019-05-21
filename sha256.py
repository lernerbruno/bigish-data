from hashlib import sha256

def file_sha256(path):
    """Return the sha256 of the file in path"""
    h = sha256()
    with open(path, 'rb') as fp:
        while True:
            data = fp.read(10*1024)
            if not data:
                break
            h.update(data)
        return h.hexdigest()
from hashlib import sha256
from time import monotonic
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def file_sha256(path):
    """Return the sha256 of the file in path"""
    h = sha256()
    with open(path, 'rb') as fp:
        while True:
            data = fp.read(10 * 1024)
            if not data:
                break
            h.update(data)
        return h.hexdigest()


def parse_signature_file(path):
    files = []
    with open(path) as fp:
        for line in fp:
            signature, name = line.split()  # unpacking
            files.append((name, signature))
    return files


def serial(signatures):
    for name, signature in signatures:
        sig = file_sha256(name)
        if sig != signature:
            print(name)


def parallel(signatures, pool):
    files = [name for name, _ in signatures]
    calculated_sigs = pool.map(file_sha256, files)
    for (name, signature), calculated in zip(signatures, calculated_sigs):
        if signature != calculated:
            print(name)


root_dir = 'data/taxi'
signatures = parse_signature_file(f'{root_dir}/sha256sum.txt')
signatures = [(f'{root_dir}/{name}', sig) for name, sig in signatures]

start = monotonic()
serial(signatures)
duration = monotonic() - start
print(f'serial took {duration:.2f} sec')

pool = ThreadPoolExecutor()
start = monotonic()
parallel(signatures, pool)
duration = monotonic() - start
print(f'parallel (thread pool) took {duration:.2f} sec')

pool = ProcessPoolExecutor()
start = monotonic()
parallel(signatures, pool)
duration = monotonic() - start
print(f'parallel (process pool) took {duration:.2f} sec')

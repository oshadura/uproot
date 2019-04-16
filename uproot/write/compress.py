#!/usr/bin/env python

# BSD 3-Clause License; see https://github.com/scikit-hep/uproot/blob/master/LICENSE

import struct
import uproot

def write_compressed(context, cursor, givenbytes, algorithm, level, key, keycursor):
    _header = struct.Struct("2sBBBBBBB")
    uncompressedbytes = len(givenbytes)
    u1 = (uncompressedbytes >> 0) & 0xff
    u2 = (uncompressedbytes >> 8) & 0xff
    u3 = (uncompressedbytes >> 16) & 0xff
    if algorithm == uproot.const.kZLIB:
        algo = b"ZL"
        import zlib
        compressedbytes = len(zlib.compress(givenbytes, level=level))
        if compressedbytes < uncompressedbytes:
            c1 = (compressedbytes >> 0) & 0xff
            c2 = (compressedbytes >> 8) & 0xff
            c3 = (compressedbytes >> 16) & 0xff
            method = 8
            cursor.write_fields(context._sink, _header, algo, method, c1, c2, c3, u1, u2, u3)
            cursor.write_data(context._sink, zlib.compress(givenbytes, level=level))
            fNbytes = compressedbytes + key.fKeylen + 9
            key.write(keycursor, context._sink, fNbytes)
        else:
            cursor.write_data(context._sink, givenbytes)
            return key.fNbytes
    elif algorithm == uproot.const.kLZ4:
        import xxhash
        algo = b"L4"
        try:
            import lz4.frame
        except ImportError:
            raise ImportError("Install lz4 package with:\n    pip install lz4\nor\n    conda install -c anaconda lz4")
        compressedbytes = len(lz4.frame.compress(givenbytes)) + 8
        if compressedbytes < uncompressedbytes:
            c1 = (compressedbytes >> 0) & 0xff
            c2 = (compressedbytes >> 8) & 0xff
            c3 = (compressedbytes >> 16) & 0xff
            method = lz4.library_version_number() // (100 * 100)
            checksum = xxhash.xxh64(givenbytes).digest()
            cursor.write_fields(context._sink, _header, algo, method, c1, c2, c3, u1, u2, u3)
            cursor.write_data(context._sink, checksum)
            cursor.write_data(context._sink, lz4.frame.compress(givenbytes, compression_level=level))
        else:
            cursor.write_data(context._sink, givenbytes)
            return key.fNbytes
        fNbytes = compressedbytes + key.fKeylen + 9
        key.write(keycursor, context._sink, fNbytes)
    elif algorithm == uproot.const.kLZMA:
        algo = b"XZ"
        try:
            import lzma
        except ImportError:
            try:
                from backports import lzma
            except ImportError:
                raise ImportError(
                    "Install lzma package with:\n    pip install backports.lzma\nor\n    conda install -c conda-forge backports.lzma\n(or just use Python >= 3.3).")
        compressedbytes = len(lzma.compress(givenbytes, preset=level))
        if compressedbytes < uncompressedbytes:
            c1 = (compressedbytes >> 0) & 0xff
            c2 = (compressedbytes >> 8) & 0xff
            c3 = (compressedbytes >> 16) & 0xff
            method = 0
            cursor.write_fields(context._sink, _header, algo, method, c1, c2, c3, u1, u2, u3)
            cursor.write_data(context._sink, lzma.compress(givenbytes, preset=level))
            fNbytes = compressedbytes + key.fKeylen + 9
            key.write(keycursor, context._sink, fNbytes)
        else:
            cursor.write_data(context._sink, givenbytes)
            return key.fNbytes
    else:
        raise ValueError("Unrecognized compression algorithm: {0}".format(algorithm))
    return fNbytes

import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
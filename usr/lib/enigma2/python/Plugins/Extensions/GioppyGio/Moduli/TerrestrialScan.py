import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))

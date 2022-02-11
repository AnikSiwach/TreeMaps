import ssl
import certifi

urlopen(request, context=ssl.create_default_context(cafile=certifi.where()))



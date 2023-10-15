import asyncio
from flick.api_service import Config
from flick.bills import Bills

config = Config('sandbox', 'your-api-key')

client = Bills(config)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(client.do_compliance_check(egs_uuid="your-egs-uuid-here"))
# Process the result the way you want
print(result)
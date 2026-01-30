import asyncio  
from livekit import api
import os

from dotenv import load_dotenv

load_dotenv()

async def main():
    lkapi = api.LiveKitAPI(
    url=os.getenv("LIVEKIT_URL"),
    api_key=os.getenv("LIVEKIT_API_KEY"),
    api_secret=os.getenv("LIVEKIT_API_SECRET"),
    )


    trunks = await lkapi.sip.list_inbound_trunk(
    api.ListSIPInboundTrunkRequest()
    )
    print(f"{trunks}")
    if trunks.items:
                in_trunk = trunks.items[0]
                in_trunk_id = in_trunk.sip_trunk_id
                print(f"Using existing inbound trunk: {in_trunk_id}")
    else:
        in_trunk = api.SIPInboundTrunkInfo(
            name=f"inbound_call",
            numbers=["74992130459"],
            krisp_enabled=True,  # если реально хотите Krips (Cloud)
        )
        request = api.CreateSIPInboundTrunkRequest(trunk=in_trunk)
        inbound_trunk = await lkapi.sip.create_sip_inbound_trunk(request)
        inbound_trunk_id = inbound_trunk.sip_trunk_id
        print(f"Created inbound trunk: {inbound_trunk_id}")

    
    rules = await lkapi.sip.list_dispatch_rule(
    api.ListSIPDispatchRuleRequest()
    )
    print(f"{rules}")
    in_trunk_id = in_trunk.sip_trunk_id

    if not rules.items:
        rule = api.SIPDispatchRule(
        dispatch_rule_individual = api.SIPDispatchRuleIndividual(
        room_prefix = 'call-',
        )
        )
        trunks = await lkapi.sip.list_inbound_trunk(
        api.ListSIPInboundTrunkRequest()
        )
        print(f"{trunks}")

        request = api.CreateSIPDispatchRuleRequest(
        dispatch_rule = api.SIPDispatchRuleInfo(
            rule = rule,
            name = 'My dispatch rule',
            trunk_ids = [in_trunk_id],
            room_config=api.RoomConfiguration(
                agents=[api.RoomAgentDispatch(
                    agent_name="assistant",
                )]
            )
        )
        )

        dispatch = await lkapi.sip.create_sip_dispatch_rule(request)

        
        print("created dispatch", dispatch)
        

        await lkapi.aclose()
            
   

  

 

asyncio.run(main())



    

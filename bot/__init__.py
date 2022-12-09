# (c) @AbirHasan2005

from dotenv import load_dotenv
import bot.client

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)

async def root_route_handler(request):

    return web.json_response("TRUMBOTS BY @FLIFHER")

async def web_server():

    web_app = web.Application(client_max_size=30000000)

    web_app.add_routes(routes)

    return web_app



load_dotenv()
bot = bot.client.Client()

import asyncio, json, random, math, time
import websockets

W, H = 100, 100
ZONES = {"red": (15,15,30,22), "yellow": (60,50,20,25)}

def inside(z, x, y):
    X,Y,Wd,Hd = z
    return X <= x <= X+Wd and Y <= y <= Y+Hd

# agenti iniziali
agents = [{"id": f"T{i+1}", "x": random.uniform(10,90), "y": random.uniform(10,90),
           "vx": random.uniform(-1,1), "vy": random.uniform(-1,1)}
          for i in range(8)]

async def handler(ws):
    print("client connesso")
    try:
        while True:
            # aggiorna posizioni
            for a in agents:
                a["x"] += a["vx"]*0.5
                a["y"] += a["vy"]*0.5
                if a["x"]<0 or a["x"]>W: a["vx"]*=-1
                if a["y"]<0 or a["y"]>H: a["vy"]*=-1
                status="ok"
                if inside(ZONES["red"],a["x"],a["y"]): status="crit"
                elif inside(ZONES["yellow"],a["x"],a["y"]): status="warn"
                a["status"]=status
            frame={"type":"frame","ts":time.time(),
                   "tags":[{"id":a["id"],"x":round(a["x"],2),"y":round(a["y"],2),"status":a["status"]} for a in agents]}
            await ws.send(json.dumps(frame))
            await asyncio.sleep(0.1)  # 10 Hz
    except:
        print("client disconnesso")

async def main():
    print("server ws://0.0.0.0:8765")
    async with websockets.serve(handler,"0.0.0.0",8765,ping_interval=None):
        await asyncio.Future()

if __name__=="__main__":
    asyncio.run(main())

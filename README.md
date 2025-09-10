# UWB DPI Live Map

Sistema di simulazione e visualizzazione in tempo reale di tag UWB e zone di sicurezza DPI.  
Progetto basato su:
- **Frontend**: GitHub Pages (canvas HTML/JS)
- **Backend simulato**: Python WebSocket server (`uwb_ws_sim.py`)
- **Tunneling**: Cloudflare Tunnel (`cloudflared`) per esporre il server locale al web

---

## 🌍 URL pubblici
- Demo simulazione interna (hardcoded):  
  👉 [https://amrierscuo.github.io/uwb-dpi-live/](https://amrierscuo.github.io/uwb-dpi-live/)
- Modalità Live (con WebSocket configurabile):  
  👉 [https://amrierscuo.github.io/uwb-dpi-live/live.html](https://amrierscuo.github.io/uwb-dpi-live/live.html)

---

## ⚙️ Requisiti
- [Python 3.10+](https://www.python.org/) con `pip`
- Modulo Python `websockets`
- [Cloudflare cloudflared](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/) installato

---

## 📦 Installazione dipendenze

```powershell
# dentro la cartella del progetto
python -m pip install websockets

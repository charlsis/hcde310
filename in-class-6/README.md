# Class 6 in-class exercise: API keys and secrets (AI: Stage 3, Little helper)

Goal: call an API that needs a key, without the key ever ending up on GitHub.

1. **Get a key.** Sign up at [api.nasa.gov](https://api.nasa.gov) (free, about a minute). The key arrives by email. Don't use `DEMO_KEY`: the whole room shares it, and it stops after 10 requests an hour.
2. **Make `.env`** in this folder with one line: `NASA_API_KEY=your_key_here` (no quotes, no spaces).
3. **Check that git ignores `.env`.** Run `git status`: `.env` should **not** show up. Your `hcde310` folder already has a `.gitignore` that lists `.env`, so it usually won't. If `.env` does show up, make a `.gitignore` in this folder with one line, `.env`, and run `git status` again. Fix it before you commit anything.
4. **Install** (with your venv on): `pip install requests python-dotenv`
5. **Fill in `earth.py`** (EPIC: photos of the whole Earth from space): load the key with `python-dotenv` (`load_dotenv()`, then `os.getenv("NASA_API_KEY")`), call `https://api.nasa.gov/EPIC/api/natural` with your key and `timeout=10`, check the status code, and print the `caption` and `date` of the first photo.
6. **Answer in `notes.md`:** What happens if you run it with a wrong key? (Try it: what status code?) Where does your key live, and why isn't it in `earth.py`?
7. **Submit:** commit and push, then submit your **commit link** on Canvas **by midnight tonight**. Before you push, check on GitHub that `.env` isn't there.

Done early? Print one more field you'd show a user, or start HW3.

Graded on completion. Stuck? Push what you have with a note in `notes.md` saying where you got stuck; that still counts.

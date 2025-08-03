import os

import onchebot
from dotenv import load_dotenv
from onchebot.models import Message, Topic
from onchebot.modules import Misc
from onchebot.redis_client import redis

load_dotenv()

REQUIRED_ENV_KEYS = [
    "ONCHE_USERNAME",
    "ONCHE_PASSWORD",
    "ONCHE_ADMIN",
    "REDIS_USERNAME",
    "REDIS_PASSWORD",
    "LOKI_URL",
]


def check_env() -> None:
    missing = [key for key in REQUIRED_ENV_KEYS if not os.environ.get(key)]
    if missing:
        raise RuntimeError(
            "Missing required environment variables: " + ", ".join(missing)
        )


check_env()

from ai import get_ai_answer, get_msg_history

onchebot.setup(
    redis_host="localhost",
    redis_port=6379,
    redis_username=os.environ.get("REDIS_USERNAME", None),
    redis_password=os.environ.get("REDIS_PASSWORD", None),
    loki_url=os.environ.get("LOKI_URL", None),
)

user = onchebot.add_user(
    username=os.environ.get("ONCHE_USERNAME", ""),
    password=os.environ.get("ONCHE_PASSWORD", ""),
)

bot = onchebot.add_bot(
    id="autobot",
    user=user,
    topic_id=782686,
    modules=[Misc(admin=os.environ.get("ONCHE_ADMIN", ""))],
)


@bot.command("/autobot")
async def on_ai(msg: Message, _):
    topic: Topic | None = await redis().get_topic(msg.topic_id)
    if not topic:
        return

    msg_history = await get_msg_history(msg)

    text = await get_ai_answer(bot, topic.title, msg, msg_history)
    if not text:
        return

    await bot.post_message(text, answer_to=msg)


onchebot.start()

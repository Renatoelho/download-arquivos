
from random import randint
from random import choice
from datetime import datetime


def cabecalho() -> dict:
    modelo_motorola = (
        "C",
        "E",
        "G",
        "X",
        "Z",
        "One",
        "Vision"
    )

    modelo_xiaomi = (
        "6",
        "7",
        "8A",
        "8 SE",
        "8T Pro",
        "9",
        "9 Pro",
        "A3",
        "S2"
    )

    modelo_smartphone = (
        [
            f"moto {choice(modelo_motorola)}",
            f"Mi {choice(modelo_xiaomi)}",
            f"Redmi {choice(modelo_xiaomi)}"
        ]
    )

    versao_windows = (
        [
            "Windows 11.0",
            "Windows 10",
            "Windows 7",
            "Windows Vista",
            "Windows XP"
        ]
    )

    distribuicao_linux = (
        [
            "Ubuntu",
            "Pop-os",
            "Fedora",
            "Debian",
            "Mint"
        ]
    )

    accept = (
        "text/html,"
        "application/xhtml+xml,"
        f"application/xml;q=0.{randint(2,8)},"
        f"image/webp,image/apng,*/*;q=0.{randint(3,9)}"
    )

    user_agent = (
        [
            (
                f"Mozilla/5.0 (Linux; Android {randint(8,13)}; "
                f"{choice(modelo_smartphone)}) "
                f"AppleWebKit/{randint(512,555)}.36 (KHTML, like Gecko) "
                f"Chrome/{randint(70,105)}.0.{randint(1,5500)}.66 "
                f"Mobile Safari/{randint(512,555)}.36"
            ),
            (
                f"Mozilla/5.0 ({choice(versao_windows)}; "
                f"Win64; x64) AppleWebKit/{randint(512,555)}.36 "
                f"(KHTML, like Gecko) Chrome/{randint(70,105)}.0"
                f".{randint(1,5500)}.128 Safari/{randint(512,555)}.36"
            ),
            (
                f"Mozilla/5.0 ({choice(distribuicao_linux)}; "
                f"Linux x86_64; rv:{randint(60,90)}.0) "
                f"Gecko/{randint(2015, int(datetime.now().strftime('%Y')))}"
                f"0101 Firefox/{randint(60,90)}.0"
            ),
            (
                f"Mozilla/5.0 (iPad; CPU OS {randint(11,15)}_2 "
                f"like Mac OS X) AppleWebKit/{randint(512,555)}.1.15 "
                "(KHTML, like Gecko) Mobile/15E148"
            ),
            (
                f"Mozilla/5.0 (iPhone; CPU iPhone OS {randint(11,15)}_2 "
                f"like Mac OS X) AppleWebKit/{randint(512,555)}.1.15 "
                f"(KHTML, like Gecko) Version/{randint(11,15)}.1 "
                f"Mobile/15E148 Safari/{randint(512,555)}.1"
            )
        ]
    )

    accept_language = (
        [
            f"en-US,en;q=0.{randint(3,9)}",
            f"pt-PT,pt;q=0.{randint(3,9)}"
            f"pt-BR,pt;q=0.{randint(3,9)}"
        ]
    )

    return (
        {
            "User-Agent": choice(user_agent),
            "Accept": accept,
            "Connection": "Keep-alive",
            "Accept-encoding": "gzip, deflate",
            "Accept-language": choice(accept_language)
        }
    )


if __name__ == "__main__":

    print(cabecalho())

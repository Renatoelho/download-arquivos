
from random import randint
from random import choice
from datetime import datetime


def cabecalho() -> dict:
    versao_motorola = (
        [
            "moto C",
            "moto E",
            "moto G",
            "moto X",
            "moto Z",
            "moto One",
            "moto Vision",
            "Mi 9 SE",
            "Mi 9T Pro",
            "Mi 8",
            "Mi 8 Pro",
            "Mi A3",
            "Redmi 8",
            "Redmi 7",
            "Redmi 6",
            "Redmi 8A",
            "Redmi S2"
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

    versao_linux = (
        [
            "Ubuntu",
            "Pop-os",
            "Fedora",
            "Debian",
            "Mint"
        ]
    )

    accept = (
        [
            (
                "text/html,"
                "application/xhtml+xml,"
                f"application/xml;q=0.{randint(5,9)},"
                f"image/webp,*/*;q=0.{randint(4,8)}"
            ),
            (
                "text/html,"
                f"application/xhtml+xml.{randint(5,9)},"
                f"application/xml.{randint(4,8)}"
            )
        ]
    )

    user_agent = (
        [
            (
                f"Mozilla/5.0 (Linux; Android {randint(8,13)}; "
                f"{choice(versao_motorola)}) "
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
                f"Mozilla/5.0 ({choice(versao_linux)}; "
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

    accept_language = ["en-US,en;q=0.5", "pt-BR,pt;q=0.3"]

    return (
        {
            "User-Agent": choice(user_agent),
            "Accept": choice(accept),
            "Connection": "Keep-alive",
            "Accept-encoding": "gzip, deflate",
            "Accept-language": choice(accept_language)
        }
    )


if __name__ == "__main__":

    print(cabecalho())

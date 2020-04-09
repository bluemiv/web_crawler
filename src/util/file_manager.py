# -*- coding: utf-8 -*-


import os


def _create_file(dest, text, encoding="utf-8"):
    """파일을 생성한다.

    :param dest: 파일 저장 경로
    :param text: 파일 내용
    :param encoding: 인코딩 값 (default: utf-8)
    :return: {boolean} 파일 생성 여부
    """
    assert not os.path.exists(dest), "Already file is exists. => path: {}".format(dest)

    with open(dest, "w", encoding=encoding) as f:
        f.write(text)

    return os.path.exists(dest) and os.path.getsize(dest)


def create_html_file(dest, text, encoding="utf-8"):
    _dest = dest if dest.endswith(".html") else dest + ".html"
    return _create_file(_dest, text, encoding=encoding)

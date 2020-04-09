#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import tempfile
import time


def _create_file(dest, text, overwrite=False, encoding="utf-8"):
    """파일을 생성한다.

    :param dest: 파일 저장 경로
    :param text: 파일 내용
    :param overwrite: 파일이 존재하면 덮어씌운다.
    :param encoding: 인코딩 값 (default: utf-8)
    :return: {boolean} 파일 생성 여부
    """
    if not overwrite and os.path.exists(dest):
        raise RuntimeError("Already file is exists. => path: {}".format(dest))

    with tempfile.TemporaryDirectory() as tmp:
        if overwrite:
            tmp_filepath = os.path.join(tmp, "{}_{}".format(time.time(), os.path.split(dest)[1]))
            os.rename(dest, tmp_filepath)

    try:
        with open(dest, "w", encoding=encoding) as f:
            f.write(text)
        if overwrite and os.path.exists(tmp_filepath):
            os.remove(tmp_filepath)
    except Exception as exc:
        if overwrite:
            os.rename(tmp_filepath, dest)  # 예상치 못한 에러 발생시 원복
        raise exc

    return os.path.exists(dest) and os.path.getsize(dest)


def create_html_file(dest, text, overwrite=False, encoding="utf-8"):
    """html 파일을 생성한다."""
    _dest = dest if dest.endswith(".html") else dest + ".html"
    assert _create_file(
        _dest, text, overwrite=overwrite, encoding=encoding), "Fail to create html file. => path: {}".format(_dest)
    return _dest


def create_css_file(dest, text, overwrite=False, encoding="utf-8"):
    """css 파일을 생성한다."""
    _dest = dest if dest.endswith(".css") else dest + ".css"
    assert _create_file(
        _dest, text, overwrite=overwrite, encoding=encoding), "Fail to create css file. => path: {}".format(_dest)
    return _dest


def create_js_file(dest, text, overwrite=False, encoding="utf-8"):
    """js 파일을 생성한다."""
    _dest = dest if dest.endswith(".js") else dest + ".js"
    assert _create_file(
        _dest, text, overwrite=overwrite, encoding=encoding), "Fail to create js file. => path: {}".format(_dest)
    return _dest


def _create_image(dest, byte_string, rename_save=False, overwrite=False):
    """이미지 파일을 저장한다.

    :param dest: 이미지 저장 경로
    :param byte_string: 바이트 스트링
    :param rename_save: 파일이 존재하면 rename 하여 저장한다. `overwrite` 보다 우선 적용된다.
    :param overwrite: 파일이 존재하면 덮어씌운다. `rename_save` 가 우선 적용된다.
    :return:
    """
    if not rename_save and not overwrite and os.path.exists(dest):
        raise RuntimeError("Already image is exists. => path: {}".format(dest))

    # 바이트 문자열이 아니면 이미지 파일이 아니다.
    assert isinstance(bytes, byte_string), "Invalid byte string for image. => path: {}".format(dest)

    # TODO rename_save 와 overwrite 기능 구현해야 함.
    with open(dest, "wb") as f:
        f.write(byte_string)

    return os.path.exists(dest) and os.path.getsize(dest)

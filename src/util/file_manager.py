#!/usr/bin/python3
# -*- coding: utf-8 -*-


import os
import random
import shutil


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

    # Overwrite
    if overwrite:
        tmp_dest = _get_new_filename(dest)
        os.rename(dest, tmp_dest)

        try:
            with open(dest, "w", encoding=encoding) as f:
                f.write(text)
            if os.path.exists(tmp_dest):
                os.remove(tmp_dest)
        except Exception as exc:
            os.rename(tmp_dest, dest)  # 예상치 못한 에러 발생시 원복
            raise exc
    else:
        with open(dest, "w", encoding=encoding) as f:
            f.write(text)

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


def _get_new_filename(filepath):
    """해당 경로에 파일이 존재하는 경우, (재귀적으로) 새로운 이름을 반환한다.

    :param filepath: 파일 경로
    :return: 새로운 이름의 파일 경로
    """
    if os.path.exists(filepath):
        base_dir, filename = os.path.split(filepath)
        rename_path = os.path.join(base_dir, "{}{}".format(random.randrange(0, 10), filename))
        return _get_new_filename(rename_path)
    else:
        return filepath


def create_image(dest, byte_string, rename_save=False, overwrite=False):
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
    assert isinstance(byte_string, bytes), "Invalid byte string for image. => path: {}".format(dest)

    # Get rename file path
    if rename_save:
        dest = _get_new_filename(dest)
        with open(dest, "wb") as f:
            f.write(byte_string)

    # Overwrite
    elif not rename_save and overwrite:
        tmp_dest = _get_new_filename(dest)
        os.rename(dest, tmp_dest)

        try:
            with open(dest, "wb") as f:
                f.write(byte_string)
            if os.path.join(tmp_dest):
                os.remove(tmp_dest)
        except Exception as exc:
            if os.path.join(tmp_dest):
                os.rename(tmp_dest, dest)
            raise exc

    # Normal
    else:
        with open(dest, "wb") as f:
            f.write(byte_string)

    return os.path.exists(dest) and os.path.getsize(dest)


def remove(path):
    """해당 경로의 파일 또는 디렉토리를 삭제한다.

    :param path:
    :return:
    """
    if os.path.exists(path):
        method = shutil.rmtree if os.path.isdir(path) else os.remove
        method(path)
    return not os.path.exists(path)

import os
import re

"""
폴더 앞에 지정된 태그 일괄 삽입하기, 삭제하기, 수정하기

"""


def add_tag_to_folders(directory, tag):
    """
    지정된 디렉토리 내 모든 폴더 앞에 태그를 추가합니다.
    :param directory: 대상 디렉토리 경로
    :param tag: 삽입할 태그
    """
    try:
        for folder_name in os.listdir(directory):
            folder_path = os.path.join(directory, folder_name)
            if os.path.isdir(folder_path):
                # 이미 태그가 포함된 폴더는 건너뜁니다.
                if folder_name.startswith(tag):
                    print(f"이미 태그가 추가된 폴더: {folder_name}")
                    continue

                # 새 이름 생성
                new_name = f"{tag}{folder_name}"
                new_path = os.path.join(directory, new_name)

                # 폴더 이름 변경
                os.rename(folder_path, new_path)
                # print(f"폴더 이름 변경: {folder_name} -> {new_name}")

        print("\n모든 폴더에 태그 삽입 완료!")
    except Exception as e:
        print(f"오류 발생: {e}")


def delete_tag_to_folders(directory):
    """
    모든 폴더의 태그 제거하기
    태그는 [], () 두 종류로 한정한다.
    """
    tag_pattern = r"^([\[\(].*?[\]\)]\s*)+"
    try:
        for folder_name in os.listdir(directory):
            folder_path = os.path.join(directory, folder_name)
            if os.path.isdir(folder_path):
                new_name = re.sub(tag_pattern, "", folder_name)
                if new_name != folder_name:
                    unique_new_name = get_unique_name(directory, new_name)
                    src = os.path.join(directory, folder_name)
                    dst = os.path.join(directory, unique_new_name)
                    try:
                        os.rename(src, dst)
                        # print(f"Renamed: {folder_name} -> {unique_new_name}")
                    except OSError as e:
                        print(
                            f"폴더명 변경 실패: '{folder_name}' -> '{unique_new_name}'. 오류: {e}"
                        )
                else:
                    print(f"태그가 제거되지 않았습니다: '{folder_name}'")

    except Exception as e:
        print(f"오류 발생: {e}")


def get_unique_name(directory, base_name):
    """
    동일한 이름의 폴더가 있을 경우, 숫자를 붙여 고유한 이름을 반환.
    """
    counter = 1
    new_name = base_name
    while os.path.exists(os.path.join(directory, new_name)):
        new_name = f"{base_name} ({counter})"
        counter += 1
    return new_name


def rename_folders_in_directory(directory, old_tag, new_tag):
    """
    지정된 디렉토리 내의 폴더 이름에서 앞에 붙은 태그를 일괄 수정합니다.

    :param directory: 대상 디렉토리 경로
    :param old_tag: 수정 대상 태그 (예: "[old]")
    :param new_tag: 변경할 태그 (예: "[new]")
    """
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory.")
        return

    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # 폴더인지 확인
        if os.path.isdir(folder_path) and folder_name.startswith(old_tag):
            # 새로운 이름 생성
            new_folder_name = folder_name.replace(old_tag, new_tag, 1)
            new_folder_path = os.path.join(directory, new_folder_name)

            # 폴더 이름 변경
            os.rename(folder_path, new_folder_path)
            # print(f"Renamed: {folder_name} -> {new_folder_name}")
        else:
            print(f"Skipped: {folder_name} (does not match tag or is not a folder)")


if __name__ == "__main__":
    print("FileTagChanger v0.1")
    print(
        "본 프로그램은 아직 개발 도중입니다. 폴더명 되돌리기 기능이 없으므로 주의하시기 바랍니다."
    )
    directory = input("대상 디렉토리 경로를 입력하세요: ").strip()
    if os.path.exists(directory) and os.path.isdir(directory):
        while 1:
            os.system("cls")
            print("FileTagChanger v0.1")
            print(
                "본 프로그램은 아직 개발 도중입니다. 폴더명 되돌리기 기능이 없으므로 주의하시기 바랍니다."
            )
            print("1. 태그 삽입하기\t2. 태그 삭제하기\t3. 태그 수정하기\t4. 끝내기")
            select = input("어떤 작업을 수행하겠습니까? : ").strip()
            if select == "1":
                insert_tag = input("삽입할 태그를 입력하세요 (예: [tag]) : ").strip()
                add_tag_to_folders(directory, insert_tag)
            elif select == "2":
                delete_tag_to_folders(directory)
            elif select == "3":
                old_tag = input("수정 대상 태그 (예: [old]) : ")
                new_tag = input("변결할 태그 (예: [new] : ")
                rename_folders_in_directory(directory, old_tag, new_tag)
            elif select == "4":
                break
    else:
        print("유효하지 않은 디렉토리 경로입니다.")

import cv2
from pathlib import Path

def class_folder_check(class_folder_path):
    assert class_folder_path.is_dir()

    class_folder = class_folder_path.name
    remove_list  = []

    # build list of files
    fnames = [f.name for f in class_folder_path.iterdir() if f.is_file()]

    # show images
    for f in fnames:
        print(f"open: {class_folder}/{f}")
        img = cv2.imread(str(class_folder_path/f))
        img = cv2.resize(img, (800,600))
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow(f'image', img) # if name changes, OpenCV will open a new window
        cv2.waitKey(1) # OpenCV needs time (> 0) to open the image; I think

        inpt = '0'
        while not inpt.isalpha() or (inpt[0].lower() not in ['y','n','q']):
            inpt = input(f"Does this belong in {class_folder}? (y/n/q:quit): ")
        inpt = str(inpt[0]).lower()

        if inpt == 'y':
            pass
        elif inpt == 'n':
            remove_list.append(f)
            print(f"{f} added to removals list.")
        elif inpt == 'q':
            break
    cv2.destroyAllWindows()

    return remove_list

path = Path().home()/'data/aircraft'
ignores = ['backup','models']
class_folders = [f for f in path.iterdir() if f.is_dir() and f.name not in ignores]
# open_image(class_folders[0]/'00000000.jpg')

class_folder_check(class_folders[0])
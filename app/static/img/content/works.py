from pathlib import Path
current_path = Path(__file__).parent

work_list =  [
        {
        'id': 1,
        'category': 'Work project',
        'title': 'Project Title',
        'description': ['First Line', 'Second Line'],
        'folder': 'folder-1',
        'group': 'proj-wk',
    },
        {
        'id': 2,
        'category': 'Study project',
        'title': 'Project Title',
        'description': ['First Line', 'Second Line', '2017'],
        'folder': 'folder-2',
        'group': 'proj-st',
    },
        {
        'id': 3,
        'category': 'Work project',
        'title': 'Project Title',
        'description': ['Description', '2016'],
        'folder': 'folder-3',
        'group': 'proj-wk',
    },
        {
        'id': 4,
        'category': 'Study project',
        'title': 'Title',
        'description': ['Info', '2015'],
        'folder': 'folder-4',
        'group': 'proj-st',
    },
        {
        'id': 5,
        'category': 'Study project',
        'title': 'Title',
        'description': ['Details', 'Info', '2019'],
        'folder': 'folder-5',
        'group': 'proj-st',
    },
        {
        'id': 6,
        'category': 'Study project',
        'title': 'Title',
        'description': ['Details', '2010'],
        'folder': 'folder-6',
        'group': 'proj-st',
    },
]

# Generate List of JPG/PNG files for each project
for work in work_list:
    folder_str = work['folder']
    folder_path = current_path.joinpath(folder_str)
    temp_list_files = (list(folder_path.rglob('*')))
    clean_list_files = list()
    for file in temp_list_files:
        file = str(file)
        if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
            index = file.find('/static')
            clean_list_files.append(file[index:])
    clean_list_files.sort()
    work['images'] = clean_list_files

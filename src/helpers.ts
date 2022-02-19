export const resetTitleAndUrl = () => {
    const title = 'Map Mods | Siege Engineers';
    window.history.pushState({}, title, window.location.protocol + '//' + window.location.host);
    document.title = title;
}

export const updateTitleAndUrl = (modId: number) => {
    const title = 'Map Mod ' + modId + ' | Siege Engineers';
    window.history.pushState({}, title, window.location.protocol + '//' + window.location.host + '/' + modId);
    document.title = title;
}

export const getSingleModId = () => {
    if (window.location.pathname === '/') {
        return null;
    }
    const items = window.location.pathname.split('/');
    return parseInt(items[1]);
}

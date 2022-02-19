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

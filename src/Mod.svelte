<script lang="ts">
    import DownloadLink from "./DownloadLink.svelte";
    import type {IMod} from "./Interfaces";
    import {singleModId} from "./stores";

    export let mod: IMod;

    const clickHandler = () => {
        singleModId.set(mod.modId);
    }
</script>

<div class="card">
    <div class="card-content">
        <div class="columns">
            <div class="column is-one-fifth">
                <figure class="image is-16by9">
                    <img loading="lazy" src="{mod.thumbnail}" alt="Thumbnail">
                </figure>
            </div>
            <div class="column">
                <h3 class="title is-4"><a href="/{mod.modId}"
                                          on:click|preventDefault={clickHandler}>{mod.modName}</a></h3>
                <h4 class="title is-6">by {mod.creatorName} <img loading="lazy" alt="creator avatar"
                                                                 class="image is-24x24 avatar"
                                                                 src="{mod.creatorAvatarUrl}"/></h4>
                <div>{@html mod.modDescription}</div>
            </div>
        </div>
    </div>
    <footer class="card-footer">
        <DownloadLink downloadUrl={mod.downloadUrl} modFileSize={mod.modFileSize}/>
        <a href="https://www.ageofempires.com/mods/details/{mod.modId}/" class="card-footer-item">View on
            ageofempires.com</a>
        <p class="card-footer-item">
            <span class="tag is-secondary" title="created">C: {mod.createDate.substring(0, 10)}</span>
            &emsp;
            <span class="tag is-secondary" title="updated">U: {mod.lastUpdate.substring(0, 10)}</span>
            &emsp;
            <span class="tag is-info">{mod.downloads.toLocaleString('en-US')} Downloads</span>
        </p>
    </footer>
</div>

<style>
    .card {
        margin-bottom: 1rem;
    }

    .avatar {
        display: inline-block;
        vertical-align: middle;
    }
</style>

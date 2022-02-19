<script lang="ts">
    import {singleModId} from "./stores";

    export let promise: Promise<{modList, lastUpdate, modCount}>;

    const clickHandler = () => {
        singleModId.set(null);
    }
</script>

<section class="hero is-success is-bold">
    <div class="hero-body">
        <div class="container">
            <h1 class="title is-2">
                <img src="/img/SiegeEngineers.png" alt="Siege Engineers"/>
                <a href="/" on:click|preventDefault={clickHandler}>Map Mods</a>
            </h1>
            <p class="subtitle">
                {#await promise}
                    Age of Empires II DE map mods list – … Mods Total – Last Update: …
                {:then resolved}
                    Age of Empires II DE map mods list – {resolved.modCount} Mods Total – Last
                    Update: {resolved.lastUpdate}
                {/await}
            </p>
        </div>
    </div>
</section>

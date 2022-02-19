<script lang="ts">
    import {singleModId} from "./stores";

    export let modCount = '…';
    export let lastUpdate = '…';

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
                Age of Empires II DE map mods list – {modCount} Mods Total – Last Update: {lastUpdate}
            </p>
        </div>
    </div>
</section>

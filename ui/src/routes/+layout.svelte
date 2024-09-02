<script lang="ts">
     import "../app.css"
     import { page } from "$app/stores"
     import { onDestroy } from "svelte"
     import Header from "../components/header/Header.svelte"
     import { SvelteKitTopLoader } from "sveltekit-top-loader"
     import type Page from "./+page.svelte"

     let currentPath: string

     const unsubscribe = page.subscribe(($page: Page) => {
          currentPath = $page.url.pathname
     })

     onDestroy(() => unsubscribe())

     /* idhar  routes likhne hai jidhar header ni dikhana */
     const noHeaderPaths: string[] = ["/login" /* <-  dekho ese */, "/signup"]

     $: showHeader = !noHeaderPaths.includes(currentPath)
</script>

{#if showHeader}
     <Header />
{/if}

<div>
     <SvelteKitTopLoader color={"#EB4F27"} />
     <slot />
</div>

<script>
     import { BottomNav, BottomNavItem } from "flowbite-svelte"
     import {
          HomeSolid,
          MessageDotsSolid,
          AdjustmentsVerticalOutline,
          UserCircleSolid,
          PlusOutline,
     } from "flowbite-svelte-icons"
     import { page } from "$app/stores"

     $: activeUrl = $page.url.pathname
</script>

<BottomNav {activeUrl} position="absolute" classInner="grid-cols-5">
     <BottomNavItem btnName="Home" href="/">
          <HomeSolid />
     </BottomNavItem>
     <BottomNavItem btnName="Chat" href="/docs/pages/quickstart" exact={false}>
          <MessageDotsSolid />
     </BottomNavItem>

     <div class="flex items-center justify-center">
          <BottomNavItem
               appBtnPosition="middle"
               btnClass="inline-flex items-center justify-center w-10 h-10 font-medium bg-primary-600 rounded-full hover:bg-primary-700 group focus:ring-4 focus:ring-primary-300 focus:outline-none dark:focus:ring-primary-800"
          >
               <PlusOutline class="text-white" />
          </BottomNavItem>
     </div>

     <BottomNavItem btnName="Settings" href="">
          <AdjustmentsVerticalOutline />
     </BottomNavItem>
     <BottomNavItem btnName="Profile" href="/profile/1">
          <UserCircleSolid />
     </BottomNavItem>
</BottomNav>

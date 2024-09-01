<script>
    import { BottomNav, BottomNavItem, Tooltip, Skeleton, ImagePlaceholder } from 'flowbite-svelte';
    import { HomeSolid, MessageDotsSolid, AdjustmentsVerticalOutline, UserCircleSolid, PlusOutline } from 'flowbite-svelte-icons';
    import { page } from '$app/stores';
    $: activeUrl = $page.url.pathname;
  </script>
  
 
  <BottomNav {activeUrl} position="absolute" classInner="grid-cols-4">
    <BottomNavItem btnName="Home" href="/">
      <HomeSolid />
    </BottomNavItem>
    <BottomNavItem btnName="Chat" href="/docs/pages/quickstart" exact={false} >
      <MessageDotsSolid />
    </BottomNavItem>
    <BottomNavItem btnName="Settings" href="/docs/components/bottom-navigation">
      <AdjustmentsVerticalOutline />
    </BottomNavItem>
    <BottomNavItem btnName="Profile" href="/profile/1">
      <UserCircleSolid />
    </BottomNavItem>
  </BottomNav>
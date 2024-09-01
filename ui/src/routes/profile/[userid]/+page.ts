import type { PageLoad } from "./$types";

export const ssr = false;

export const load: PageLoad = ({ params }) => {
  const { userid } = params;

  console.log(userid);

  return {
    userid,
  };
};

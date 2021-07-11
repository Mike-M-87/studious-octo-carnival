let color = '#3aa757';
let d = 0;
chrome.runtime.onInstalled.addListener(() => {
  chrome.storage.sync.set({ color });
  setInterval(()=>{
	 d++;
	 console.log(d)
  },1000)
  console.log('Default background color set to %cgreen', `color: ${color}`);
});

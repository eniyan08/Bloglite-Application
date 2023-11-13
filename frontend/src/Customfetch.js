export default async function Customfetch(url, init_obj){
    let res = null
    let data = null
    try{
        res = await fetch(url, init_obj)
    }catch{
        throw new Error("network connection failed")
    }
    try{
        data = await res.json()
    }catch{
        throw new Error("Response body was not json")
    }
    if(res.ok){
        return data
    }else{
        throw new Error(data.message)
    }

}
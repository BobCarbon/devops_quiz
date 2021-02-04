Alternative methods:

## ModHeader
1. Run default browser
    - Ideally Chrome or Firefox, latest versions
2. Install "ModHeader" plugin/extension
3. Launch ModHeader
4. Create request profile
5. Add "Pragma" header, with value "no-cache"
6. Perform request to server/URL with updated request context


## Postman
1. Run Postman
2. Create new GET session
3. Add desired server/endpoint/URL
4. Go to 'Headers' tab
    - Remove any default/non-essential headers
    - Add header with key: "Pragma" and value: "no-cache"
5. Send GET request

# AD User Provisioner

The idea of this program is to help automate the creation of users in Active Directory. 

This tool will use a configuration file allowing people to select from a list of approved options when it comes to things like department, office, etc. This should ensure that there is less chance of a user's configuration being a problem in the future. Standardising in this way should also help with other areas of automation; one that springs to mind is dynamic groups in Azure AD which allows you to automatically put people in certain AD groups depending on their user attributes. This can be difficult if there is no control over how attributes are input, or which ones are filled.

The program is now in a working state!

## Usage

So this repo contains the code as well as the application packaged as an exe file. If you'd like to change the application to suit your needs feel free. 

The folder "packagedApp" contains the exe and the config folder. You can take these two and use it as much as you want. 

Most of the fields are fairly self explanatory. Once you've filled in the required fields the "Create User" button will be clickable. 

The Company, Department, and Job Title dropdown boxes are populated using the config file in the config directory. I should just move the file out of the directory as it's superfluous but I've not done it yet. The file is a fairly simple json file containing these items, I've made this hierarchical as I think it makes sense; normally if you have different companys, even in the same industry, they're likely to have slightly different department names. Below is the default layout. 

```json
{
    "Construction" : [

    ],
    
    "Interiors": [

    ],

    "Holdings": [ 
            {
                "deptName": "Information Technology",
                "roles": ["IT Security Analyst", "Hosting and Storage Analyst", "Hosting and Storage Engineer", "Role does not exist"]
            },
            {
                "deptName": "People Team",
                "roles": ["Principal Group People Manager", "Group People Manager", "Role does not exist"]
            },
            {
                "deptName": "Company Secretary"
            }
    ]
}
```

For transparency, the top level of the file is the company. The deptName is the department. And the roles are the job titles. As you can see you can have many roles in a department, and many departments in a company. 

I'd recommend filling at least one of each; this will add some clarity to your AD and will allow you to do things based on people's teams. If the config file isn't there the program will not run. 

The manager field is a bit of an odd one and this is mainly because of the way AD uses this field; I thought about removing it, but I think it has some good uses. The manager **must** exist in AD for it to be selected, and you **must** use their Pre2k logon name to find them. I've included a button to check that the manager you are querying exists so you don't get any errors when using the create user button. 

The employee number field isn't functional at the moment...

The password is obviously where you enter the user's first password.

The organisational unit will populate when the program is run. It gets this buy querying your AD structure from the top. 

The two check boxe can force the user to change their password, or stop it from expiring. You can't have both of these checked, but you can have neither of them checked. 

The check for duplicates button will check if you trying to create a user with a pre2k, or a user logon name that already exists. This is something AD won't allow, so the button just pre-empts the error. 

The "Create Powershell Cmd" button is one that I included just to show what the command is. This allows you to review the command before it runs. It also gives you the opportunity to change the command if you want to add/remove items or to review if there is an error. This button can be pressed at any point and a command will be output.

Finally the "Create User" button will create the user. If you do not have permissions to create users this will not work.

If you do not have read permissions on your AD instance this program will likely not function properly as it reads from AD for a few things, like the OU structure, and when you're using the two buttons to check different elements.
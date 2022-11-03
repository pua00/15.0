<record id="server_action_change_doctor_multy_wizard" model="ir.actions.server">
        <field name="name">Wizard for easy way to change doctor</field>
        <field name="model_id" ref="model_change_doctor_multy_wizard"/>
        <field name="state">code</field>
        <field name="code">
            action = model.action_open_wizard()
        </field>
    </record>

    <record id="menu_change_doctor_multy_wizard" model="ir.ui.menu">
        <field name="name">Wizard for easy way to change doctor</field>
        <field name="parent_id" ref="hr_hospital_patient_catalog_menu"/>
        <field name="action" ref="server_action_change_doctor_multy_wizard"/>
        <field name="sequence" eval="500"/>

    </record>


